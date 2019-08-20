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
                Tihe rezane (neuspešne) 
            </td>
       
        </tr>       
        <tr>    
            <td>
                <form action="/ScoreBoard/napovedi_nasprotnika" method="post">
                  <input type="checkbox" name="tiha_neuspesna" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="tiha_neuspesna" value="T"> Trula <br>
                  <input type="checkbox" name="tiha_neuspesna" value="P"> Pagat ultimo<br>
                  <input type="checkbox" name="tiha_neuspesna" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="tiha_neuspesna" value="V"> Valat <br>
                  <input type="submit" value="Nadaljuj">
                </form>
            </td>
        </tr>
    </table>

</html>