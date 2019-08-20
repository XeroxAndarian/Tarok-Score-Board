% import model
<!DOCTYPE html>
<html>

<head>
    <title>Tarok Score Board</title>
</head>

<body>

    <table border="0.1" cellspacing="10">
        <tr>
            <td>
               Ime
            </td>
            <td>
                {{p1}}
            </td>
            <td>
                {{p2}}
            </td>
            <td>
                {{p3}}
            </td>
            <td>
                {{p4}}
            </td>
            <td>
                
        </tr>

        <tr>
            <td>
                Št. radlcov
            </td>


            <td>
                {{Radlc1}}
            </td>
            <td>
                {{Radlc2}}
            </td>
            <td>
                {{Radlc3}}
            </td>
            <td>
                {{Radlc4}}
            </td>
        </tr>

        
        <tr>
            <td>
                Točke
            </td>

            <td>
                {{Točke1}}
            </td>
            <td>
                {{Točke2}}
            </td>
            <td>
                {{Točke3}}
            </td>
            <td>
                {{Točke4}}
            </td>
        </tr>
    </table>

    <form action="/ScoreBoard/igralec/" method="POST">
            
        <input type="submit" value="Dodaj Partijo">
    </form>
    

</body>

</html>