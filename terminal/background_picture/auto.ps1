$path = Resolve-Path ((Convert-Path . )+"\image.png")
set-itemproperty -path "HKCU:Control Panel\Desktop" -name WallPaper -value $path