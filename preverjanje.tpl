% import model
<!DOCTYPE html>
<html>
    <table>
        <tr>
            <td>
                Igralec
            </td>
            <td>
                {{igralec}}
            </td>
        </tr>

        <tr>
            <td>
                Igra
            </td>
            <td>
                {{igra}}
            </td>
        </tr>

        <tr>
            <td>
                Partner
            </td>
            <td>
                {{partner}}
            </td>
        </tr>

        <tr>
            <td>
                Točke
            </td>
            <td>
                {{tocke}}
            </td>
        </tr>

        <tr>
            <td>
                Izvedene napovedi
            </td>
            <td>
                {{napovedi}}
            </td>
        </tr>        

        <tr>
            <td>
                Rezane napovedi
            </td>
            <td>
                {{napovedi_fail}}
            </td>
        </tr>

        <tr>
            <td>
                Tihe napovedi
            </td>
            <td>
                {{napovedi_tihe}}
            </td>
        </tr>

        <tr>
            <td>
                Tihe rezane napovedi
            </td>
            <td>
                {{napovedi_tihe_rezane}}
            </td>
        </tr>

        <tr>
            <td>
                Nasprotnikove izvedene napovedi
            </td>
            <td>
                {{napovedi_nasprotnik}}
            </td>
         </tr>

         <tr>
            <td>
                Nasprotnikove rezane napovedi   
            </td>
            <td>
                {{nasprotnik_rezane}}
            </td>
        </tr>

        <tr>
            <td>
                Nasprotnikove izvedene tihe napovedi
            </td>
            <td>
                {{nasprotnik_tihe}}
            </td>
        </tr>

        <tr>
            <td>
                Nasprotnikove rezane tihe napovedi
            </td>
            <td>
                {{napovedi_nasprotnika_tihe_rezane}}
            </td>
        </tr>

        <tr>
            <td>
                Kontra
            </td>
            <td>
                {{kontra}}
            </td>
        </tr>

        <tr>
            <td>
                Mond fang
            </td>
            <td>
                {{mond_fang}}
            </td>
        </tr>


    </table>
    <table>
    <tr>
    <td>
    <form method="post" action="/ScoreBoard/racunanje">
        <input type="submit" value="Potrdi">
    </form>
    </td>
    <td>
    <form action="/ScoreBoard/igralec/" method="POST">
            
    <input type="submit" value="Ponoven Vnos">
    </form>
    </td>
    </tr>
    </table>
    


</html>