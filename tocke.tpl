% import model
<!DOCTYPE html>
<html>
    <table>        
        
        <tr>
            <td>
                Vpišite točno število točk, ki jih je igralec dosegel:
            </td>
        </tr>

        <tr>
            <td>
                <form meethod="post" action="/ScoreBoard/napovedi_uspesne" method="POST">

                <input type="text" name = "tocke" >
                <input type="submit" value="Nadaljuj">
                </form>
            </td>
        </tr>

        

    </table>
</html>