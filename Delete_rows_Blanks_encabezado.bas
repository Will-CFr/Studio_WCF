'vamos a eliminar filas que tengan en la columna con nombre de encabezado Type Comments en blanco

sub delete_rows_Blanks_encabezado()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    Dim headerCol As Long

    ' hoja de trabajo activa
    Set ws = ThisWorkbook.ActiveSheet

    ' encontrar la última fila con datos en la hoja
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    ' Encontrar la columna del encabezado que contenga la palabra "Type Comments"
    headerCol = 0
    For i = 1 To ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
        If InStr(1, ws.cells(1, i).Value, "Type Comments", vbTextCompare) > 0 Then
            headerCol = i
            Exit For
        End If
    Next i

    ' si no se encuentra la columna, salir del sub
    If headerCol = 0 Then
        MsgBox "No se encontró la columna 'Type Comments'.", vbExclamation
        Exit Sub
    End If
    
    ' recorrer las filas desde la última hasta la primera
    For i = lastRow To 2 Step -1
        If IsEmpty(ws.Cells(i, headerCol).Value) Then
            ws.Rows(i).Delete
        End If
    Next i
    
    MsgBox "Filas con 'Type Comments' en blanco han sido eliminadas.", vbInformation

End sub

