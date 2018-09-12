Option Explicit

Const vbHide = 0 'ウィンドウを非表示

Function ArgsToString()
   Const DELIMITER = " "
   Dim ret
   Dim i
   Dim n

   ret = ""
   n = Wscript.Arguments.Count
   If n > 0 Then
     For i = 1 To n
       If i < n Then
         ret = ret & Wscript.Arguments(i - 1) & DELIMITER
       Else
         ret = ret & Wscript.Arguments(i - 1)
       End If
     Next
   End If
   ArgsToString = ret
End Function

Dim rootPath
Dim fso
Set fso = createObject("Scripting.FileSystemObject")
rootPath = fso.getParentFolderName(WScript.ScriptFullName)

CreateObject("Wscript.Shell").run rootPath & "\Code.exe --user-data-dir " & rootPath & "\data  --extensions-dir " & rootPath & "\data\extensions " & ArgsToString(), vbHide
