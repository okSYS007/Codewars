param(
    [string]$Path = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"
$workspace = (Resolve-Path -LiteralPath $Path).Path
Set-Location -LiteralPath $workspace

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

function Get-LatestKataFile {
    $file = Get-ChildItem -LiteralPath $workspace -Filter "*.py" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if ($file) {
        return $file.FullName
    }

    return ""
}

function Add-Log {
    param([string]$Message)

    $timestamp = Get-Date -Format "HH:mm:ss"
    $logBox.AppendText("[$timestamp] $Message`r`n")
}

function Invoke-LoggedCommand {
    param(
        [string]$FilePath,
        [string[]]$Arguments
    )

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo.FileName = $FilePath
    $process.StartInfo.Arguments = ($Arguments | ForEach-Object {
        if ($_ -match "\s") { '"' + ($_ -replace '"', '\"') + '"' } else { $_ }
    }) -join " "
    $process.StartInfo.WorkingDirectory = $workspace
    $process.StartInfo.UseShellExecute = $false
    $process.StartInfo.RedirectStandardOutput = $true
    $process.StartInfo.RedirectStandardError = $true
    $process.StartInfo.CreateNoWindow = $true

    [void]$process.Start()
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()

    if ($stdout.Trim()) {
        Add-Log $stdout.Trim()
    }
    if ($stderr.Trim()) {
        Add-Log $stderr.Trim()
    }

    return $process.ExitCode
}

function Get-SelectedFile {
    $file = $fileBox.Text.Trim()
    if (-not $file) {
        throw "Choose a kata file first."
    }
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
        throw "File does not exist: $file"
    }
    return (Resolve-Path -LiteralPath $file).Path
}

function Invoke-Action {
    param([scriptblock]$Action)

    try {
        & $Action
    }
    catch {
        Add-Log "ERROR: $($_.Exception.Message)"
    }
}

$form = New-Object System.Windows.Forms.Form
$form.Text = "Codewars Helper"
$form.StartPosition = "CenterScreen"
$form.Size = New-Object System.Drawing.Size(820, 520)
$form.MinimumSize = New-Object System.Drawing.Size(720, 440)

$font = New-Object System.Drawing.Font("Segoe UI", 10)
$form.Font = $font

$fileLabel = New-Object System.Windows.Forms.Label
$fileLabel.Text = "Kata file"
$fileLabel.Location = New-Object System.Drawing.Point(16, 18)
$fileLabel.Size = New-Object System.Drawing.Size(90, 24)
$form.Controls.Add($fileLabel)

$fileBox = New-Object System.Windows.Forms.TextBox
$fileBox.Location = New-Object System.Drawing.Point(110, 16)
$fileBox.Size = New-Object System.Drawing.Size(560, 28)
$fileBox.Anchor = "Top,Left,Right"
$fileBox.Text = Get-LatestKataFile
$form.Controls.Add($fileBox)

$browseButton = New-Object System.Windows.Forms.Button
$browseButton.Text = "Browse"
$browseButton.Location = New-Object System.Drawing.Point(684, 14)
$browseButton.Size = New-Object System.Drawing.Size(100, 32)
$browseButton.Anchor = "Top,Right"
$browseButton.Add_Click({
    Invoke-Action {
        $dialog = New-Object System.Windows.Forms.OpenFileDialog
        $dialog.InitialDirectory = $workspace
        $dialog.Filter = "Python files (*.py)|*.py|All files (*.*)|*.*"
        if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
            $fileBox.Text = $dialog.FileName
        }
    }
})
$form.Controls.Add($browseButton)

$pushButton = New-Object System.Windows.Forms.Button
$pushButton.Text = "Push to Git"
$pushButton.Location = New-Object System.Drawing.Point(16, 62)
$pushButton.Size = New-Object System.Drawing.Size(150, 42)
$pushButton.Add_Click({
    Invoke-Action {
        $file = Get-SelectedFile
        $name = [System.IO.Path]::GetFileNameWithoutExtension($file)
        Add-Log "Pushing $name..."
        Invoke-LoggedCommand "git" @("add", "--", $file) | Out-Null
        $commitCode = Invoke-LoggedCommand "git" @("commit", "-m", "kata: update $name")
        if ($commitCode -eq 0) {
            Invoke-LoggedCommand "git" @("push") | Out-Null
        }
        else {
            Add-Log "Nothing committed or git commit failed."
        }
    }
})
$form.Controls.Add($pushButton)

$convertButton = New-Object System.Windows.Forms.Button
$convertButton.Text = "Refactor Tests"
$convertButton.Location = New-Object System.Drawing.Point(182, 62)
$convertButton.Size = New-Object System.Drawing.Size(150, 42)
$convertButton.Add_Click({
    Invoke-Action {
        $file = Get-SelectedFile
        Add-Log "Converting Codewars tests..."
        Invoke-LoggedCommand "uv" @("run", "python", ".\scripts\convert_codewars_tests.py", $file) | Out-Null
    }
})
$form.Controls.Add($convertButton)

$runButton = New-Object System.Windows.Forms.Button
$runButton.Text = "Run Tests"
$runButton.Location = New-Object System.Drawing.Point(348, 62)
$runButton.Size = New-Object System.Drawing.Size(150, 42)
$runButton.Add_Click({
    Invoke-Action {
        $file = Get-SelectedFile
        Add-Log "Running local tests..."
        Invoke-LoggedCommand "uv" @("run", "python", $file) | Out-Null
    }
})
$form.Controls.Add($runButton)

$solveButton = New-Object System.Windows.Forms.Button
$solveButton.Text = "Solve Task"
$solveButton.Location = New-Object System.Drawing.Point(514, 62)
$solveButton.Size = New-Object System.Drawing.Size(150, 42)
$solveButton.Add_Click({
    Invoke-Action {
        $file = Get-SelectedFile
        $prompt = "Solve the Codewars task in this file: $file. Add the solution, local run_tests cases, and verify them."
        [System.Windows.Forms.Clipboard]::SetText($prompt)
        Add-Log "Solve prompt copied to clipboard. Paste it into Codex chat."
    }
})
$form.Controls.Add($solveButton)

$refreshButton = New-Object System.Windows.Forms.Button
$refreshButton.Text = "Latest File"
$refreshButton.Location = New-Object System.Drawing.Point(680, 62)
$refreshButton.Size = New-Object System.Drawing.Size(104, 42)
$refreshButton.Anchor = "Top,Right"
$refreshButton.Add_Click({
    Invoke-Action {
        $fileBox.Text = Get-LatestKataFile
        Add-Log "Selected latest kata file."
    }
})
$form.Controls.Add($refreshButton)

$logBox = New-Object System.Windows.Forms.TextBox
$logBox.Location = New-Object System.Drawing.Point(16, 124)
$logBox.Size = New-Object System.Drawing.Size(768, 330)
$logBox.Anchor = "Top,Bottom,Left,Right"
$logBox.Multiline = $true
$logBox.ScrollBars = "Vertical"
$logBox.ReadOnly = $true
$logBox.Font = New-Object System.Drawing.Font("Consolas", 10)
$form.Controls.Add($logBox)

Add-Log "Workspace: $workspace"
Add-Log "Choose a file, then use Push, Refactor Tests, or Run Tests."

[void]$form.ShowDialog()
