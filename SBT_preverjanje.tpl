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
                Solo brez talona je 
            </td>
            <td>
                {{o}}
            </td>
        </tr>

        <tr>
            <td>
                Kontre
            </td>
            <td>
                {{kontra}}
            </td>
        </tr>

        <tr>
            <td>
                <form method="post" action="/ScoreBoard/racunanje_SBT">
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