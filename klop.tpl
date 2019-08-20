% import model
<!DOCTYPE html>
<html>
    <table>
        <tr>
            <td> 
                Če je kateri od igralcev "poln", pritisnite gumb z njegovim imenom pod napsom Poln. Prazen igralec je pobral 0 točk. 
            </td>
        </tr>
    </table>
    <table>
        <tr>
            
            <td>
                 Točke
            </td>

            <td>
                    Poln
            </td>
           
        </tr>

        <tr>
            

            <td>
                <form method="post" action="/ScoreBoard/klop_preverjanje">
                <input type="text" name="p1" value="{{p1}}"> <br>
                <input type="text" name="p2" value="{{p2}}"> <br>
                <input type="text" name="p3" value="{{p3}}"> <br>
                <input type="text" name="p4" value="{{p4}}"> <br>
                
                <input type="submit" value="Naprej">
                
                </form>
            </td>

            <td>
                <form method="post" action="/ScoreBoard/klop_preverjanje">
                <input type="submit" name="poln" value="{{p1}}"> <br>
                <input type="submit" name="poln" value="{{p2}}"> <br>
                <input type="submit" name="poln" value="{{p3}}"> <br>
                <input type="submit" name="poln" value="{{p4}}"> <br>
                
                </form>
            </td>


        </tr>

        




    </table>

</html>