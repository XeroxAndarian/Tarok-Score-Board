% import model
<!DOCTYPE html>
<html> 

    <table>
        <tr>
            <td>
                Igralec
            </td>
            <td>
                Točke
            </td>
        </tr>

        <tr>
            <td>
                {{p1}} 
            </td>
            <td>
                {{tocke1}}
            </td>
        </tr>

        <tr>
                <td>
                    {{p2}} 
                </td>
                <td>
                    {{tocke2}}
                </td>
            </tr>

            <tr>
                    <td>
                        {{p3}} 
                    </td>
                    <td>
                        {{tocke3}}
                    </td>
                </tr>

                <tr>
                        <td>
                            {{p4}} 
                        </td>
                        <td>
                            {{tocke4}}
                        </td>
                    </tr>


        <tr>
            <td>
                <form method="post" action="/ScoreBoard/racunanje_klop">
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