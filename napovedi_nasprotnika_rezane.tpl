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
                Neuspešne nasprotnikove (rezane)
            </td>
       
        </tr>       
        <tr>    
            <td>
                <form method="post" action="/ScoreBoard/napovedi_nasprotnika_tihi" >
                  <input type="checkbox" name="nasprotnik_rezane" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="nasprotnik_rezane" value="T"> Trula <br>
                  <input type="checkbox" name="nasprotnik_rezane" value="P"> Pagat ultimo<br>
                  <input type="checkbox" name="nasprotnik_rezane" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="nasprotnik_rezane" value="V"> Valat <br>
                  <input type="submit" value="Nadaljuj">
                </form>
            </td>
        </tr>
    </table>

</html>