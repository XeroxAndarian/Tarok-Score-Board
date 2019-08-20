% import model
<!DOCTYPE html>
<html>

<head>
    <title>Tarok Score Board</title>
</head>

<body>


    <table>
        <tr>
            <td>
               Za pričetek nove igre pritisnite gumb in vpišite imena igralcev.
            </td>
        </tr>
    </table>
    <table cellspacing="10">

        <tr>
            <form action="/ScoreBoard/" method="POST">

                <input type="text" name = "p1" value="Ime igralca 1"> <br>
                <input type="text" name = "p2" value="Ime igralca 2"> <br>
                <input type="text" name = "p3" value="Ime igralca 3"> <br>
                <input type="text" name = "p4" value="Ime igralca 4"> <br>
                <input type="submit" value="Nova Igra">
            </form>

            <form action="/Custom/" method="post">
                <input type="submit" value="Ročno vnašanje">
            </form>

            
        </tr>
    </table>
    


</body>

</html>