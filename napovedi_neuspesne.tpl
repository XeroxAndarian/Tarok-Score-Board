% import model
<!DOCTYPE html>
<html>
    <table>        
        
        <tr>
            <td>
                Napovedi:
            </td>
        </tr>
        <tr>
            <td>
                Neuspešne (rezane)
            </td>
       
        </tr>
        
        <tr>
            <td>
                <form method="post" action="/ScoreBoard/napovedi_tihe">
                  <input type="checkbox" name="napoved_fail" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="napoved_fail" value="T"> Trula <br>
                  <input type="checkbox" name="napoved_fail" value="P"> Pagat ultimo<br>
                  <input type="checkbox" name="napoved_fail" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="napoved_fail" value="V"> Valat <br>
                  <input type="checkbox" name="napoved_fail" value="BV"> Barvni Valat
                
            </td>
        </tr>
        <tr>
            <td>
                <input type="submit" value="Nadaljuj">
                </form>
            <td>
        </tr>

        

        
    </table>
</html>