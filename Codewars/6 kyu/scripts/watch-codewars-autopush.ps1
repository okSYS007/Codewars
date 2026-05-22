param(
    [string]$Path = (Resolve-Path "$PSScriptRoot\..").Path,
    [int]$DebounceSeconds = 4,
    [string]$Branch = ""
)

$ErrorActionPreference = "Stop"

function Invoke-GitAutopush {
    param([string]$ChangedPath)

    if (-not (Test-Path -LiteralPath $ChangedPath -PathType Leaf)) {
        return
    }

    $extension = [System.IO.Path]::GetExtension($ChangedPath)
    if ($extension -ne ".py") {
        return
    }

    $relativePath = Resolve-Path -LiteralPath $ChangedPath -Relative
    $status = git status --porcelain -- "$ChangedPath"
    if ([string]::IsNullOrWhiteSpace($status)) {
        return
    }

    git add -- "$ChangedPath"

    $fileName = [System.IO.Path]::GetFileNameWithoutExtension($ChangedPath)
    $message = "kata: update $fileName"
    git commit -m $message

    if ([string]::IsNullOrWhiteSpace($Branch)) {
        git push
    }
    else {
        git push origin $Branch
    }

    Write-Host "Pushed $relativePath"
}

Write-Host "Watching $Path for Python kata changes. Press Ctrl+C to stop."

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
                Invoke-GitAutopush -ChangedPath $changedPath
            }
            catch {
                Write-Warning "Autopush failed for ${changedPath}: $($_.Exception.Message)"
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
