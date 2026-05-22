param(
    [string]$Path = (Resolve-Path "$PSScriptRoot\..").Path,
    [int]$DebounceSeconds = 2
)

$ErrorActionPreference = "Stop"
$Path = (Resolve-Path -LiteralPath $Path).Path
Set-Location -LiteralPath $Path

function Convert-CodewarsTestsIfNeeded {
    param([string]$ChangedPath)

    if (-not (Test-Path -LiteralPath $ChangedPath -PathType Leaf)) {
        return
    }

    if ([System.IO.Path]::GetExtension($ChangedPath) -ne ".py") {
        return
    }

    $content = Get-Content -Raw -LiteralPath $ChangedPath
    if ($content -notmatch "test\.assert_equals\(") {
        return
    }

    uv run python "$PSScriptRoot\convert_codewars_tests.py" "$ChangedPath"
}

Write-Host "Watching $Path for pasted Codewars tests. Press Ctrl+C to stop."

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $Path
$watcher.Filter = "*.py"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

$pending = @{}

$action = {
    $fullPath = $Event.SourceEventArgs.FullPath
    $eventType = $Event.SourceEventArgs.ChangeType
    if ($eventType -eq [System.IO.WatcherChangeTypes]::Deleted) {
        return
    }

    $script:pending[$fullPath] = Get-Date
}

$created = Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action
$changed = Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action
$renamed = Register-ObjectEvent -InputObject $watcher -EventName Renamed -Action $action

try {
    while ($true) {
        Start-Sleep -Seconds 1
        $now = Get-Date
        $ready = @()

        foreach ($item in $pending.GetEnumerator()) {
            if (($now - $item.Value).TotalSeconds -ge $DebounceSeconds) {
                $ready += $item.Key
            }
        }

        foreach ($changedPath in $ready) {
            $pending.Remove($changedPath)
            try {
                Convert-CodewarsTestsIfNeeded -ChangedPath $changedPath
            }
            catch {
                Write-Warning "Test conversion failed for ${changedPath}: $($_.Exception.Message)"
            }
        }
    }
}
finally {
    Unregister-Event -SourceIdentifier $created.Name -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier $changed.Name -ErrorAction SilentlyContinue
    Unregister-Event -SourceIdentifier $renamed.Name -ErrorAction SilentlyContinue
    $watcher.Dispose()
}
