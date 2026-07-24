Sub Get_size_Quantity()

    Dim wbase As Workbook
    Dim wbase As Worksheet
    Dim wsMain As Worksheet

    Dim lastRowBase As Long
    Dim lastRowMain As Long

    Dim basePath As String

    Dim arrBase As Variant
    Dim arrMain As Variant

    Dim dict As Object

    Dim i As Long

    Dim rawSize As String
    Dim cleanSize As String

    Dim resultArr() As Variant

    '----
    ' HOJA PRINCIPAL activa
    '----

    Set wsMain = ThisWorkbook.ActiveSheet
    
    'BASE PATH

    basePath = "C:\Users\COLD-BIM4\Documents\WCHF\DiRootsone\BASE_DIMENSION_PIPE_FITTINGS.xlsx"

    