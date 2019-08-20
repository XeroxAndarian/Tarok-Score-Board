% import model
<!DOCTYPE html>
<html>
    <table>      

        <tr>
            <td>
                Partner (če je bil solo ali pa se je zarufal izberete igralca, ki je igral):
            </td>
        </tr>

        <tr>
            <td>
                <form action="/ScoreBoard/kontre" method="post">
                  <input type="submit" name="partner" value="{{p1}}"> <br>
                  <input type="submit" name="partner" value="{{p2}}"> <br>
                  <input type="submit" name="partner" value="{{p3}}">  <br>
                  <input type="submit" name="partner" value="{{p4}}">  <br>

                </form>
            </td>
        </tr>
    </table>
</html>