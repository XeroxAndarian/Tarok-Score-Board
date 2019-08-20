% import model
<!DOCTYPE html>
<html>
    <table>

        <tr>
            <td>
                Izberite igralca, ki je igral
            </td>
        </tr>

        <tr>
            <td>
                <form method="post" action="/ScoreBoard/igra">
                  <input type="submit" name="igralec" value="{{p1}}"> <br>
                  <input type="submit" name="igralec" value="{{p2}}"> <br>
                  <input type="submit" name="igralec" value="{{p3}}"> <br>
                  <input type="submit" name="igralec" value="{{p4}}"> <br>

                </form>
            </td>
        </tr>
        <tr>
            <td>
                <form method="post" action="/ScoreBoard/klop">
                  <input type="submit" value="Klop">
                </form>
            </td>
        </tr>

         

    </table>
</html>