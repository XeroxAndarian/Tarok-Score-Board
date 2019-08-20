% import model
<!DOCTYPE html>
<html>
    <table>
        <tr>
            <td>
                Izberite igro, ki jo je igral.
            </td>
        </tr>

        <tr>
            <td>
                <form method="post" action="/ScoreBoard/tocke">
                  <input type="submit" name="igra" value="Tri">  <br>
                  <input type="submit" name="igra" value="Dva">  <br>
                  <input type="submit" name="igra" value="Ena">  <br>
                  <input type="submit" name="igra" value="Solo tri"><br>
                  <input type="submit" name="igra" value="Solo dva">  <br>
                  <input type="submit" name="igra" value="Solo ena">  <br>
                </form>
                <form method="post" action="/ScoreBoard/berac">
                  <input type="submit" name="igra" value="Berač">
                </form>
                <form method="post" action="/ScoreBoard/SBT">
                  <input type="submit" name="igra" value="Solo brez talona">
                </form>
                <form method="post" action="/ScoreBoard/OB">
                  <input type="submit" name="igra" value="Odprti berač">  <br>
                </form>
            </td>
        <tr/>

        

        


    </table>
</html>