% import model
<!DOCTYPE html>
<html>
    <table>

        <tr>
            <td>
                Označite igralca, ki je igral
            </td>
        </tr>

        <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="radio" name="igralec" value="p1"> p1 <br>
                  <input type="radio" name="igralec" value="p2"> p2 <br>
                  <input type="radio" name="igralec" value="p3"> p3  <br>
                  <input type="radio" name="igralec" value="p4"> p4 <br>
                  <input type="radio" name="igralec" value="other"> Klop <br>
                </form>
            </td>
        </tr>

        <tr>
            <td>
                Označite igro, ki jo je igral
            </td>
        </tr>

        <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="radio" name="igra" value="3"> Tri <br>
                  <input type="radio" name="igra" value="2"> Dva <br>
                  <input type="radio" name="igra" value="1"> Ena <br>
                  <input type="radio" name="igra" value="S3"> Solo tri <br>
                  <input type="radio" name="igra" value="S2"> Solo dva <br>
                  <input type="radio" name="igra" value="S1"> Solo ena <br>
                  <input type="radio" name="igra" value="B"> Berač <br>
                  <input type="radio" name="igra" value="SBT"> Solo brez talona <br>
                  <input type="radio" name="igra" value="OB"> Odprti berač <br>
                </form>
            </td>
        <tr/>

        <tr>
            <td>
                Točke:
            </td>
        </tr>

        <tr>
            <td>
                <form action="/ScoreBoard/racunanje/" method="POST">

                <input type="text" name = "tocke" >
                </form>
            </td>
        </tr>

        <tr>
            <td>
                Partner:
            </td>
        </tr>

        <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="radio" name="partner" value="p1"> p1<br>
                  <input type="radio" name="partner" value="p2"> p3<br>
                  <input type="radio" name="partner" value="p3"> p3 <br>
                  <input type="radio" name="partner" value="p4"> p4
                </form>
            </td>
        </tr>

        <tr>
            <td>
                Napovedi:
            </td>
        </tr>
        <tr>
            <td>
                Uspešne 
            </td>

            <td>
                Tihe
            </td>
        
            <td>
                Neuspešne 
            </td>        
        </tr>
        
        <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="uspešna_napoved" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="uspešna_napoved" value="T"> Trula <br>
                  <input type="checkbox" name="uspešna_napoved" value="P"> Pagat <br>
                  <input type="checkbox" name="uspešna_napoved" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="uspešna_napoved" value="V"> Valat <br>
                  <input type="checkbox" name="uspešna_napoved" value="BV"> Barvni Valat
                </form>
            </td>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="tiha" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="tiha" value="T"> Trula <br>
                  <input type="checkbox" name="tiha" value="P"> Pagat <br>
                  <input type="checkbox" name="tiha" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="tiha" value="V"> Valat 
                </form>
            </td>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="neuspešna_napoved" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="neuspešna_napoved" value="T"> Trula <br>
                  <input type="checkbox" name="neuspešna_napoved" value="P"> Pagat <br>
                  <input type="checkbox" name="neuspešna_napoved" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="neuspešna_napoved" value="V"> Valat <br>
                  <input type="checkbox" name="neuspešna_napoved" value="BV"> Barvni Valat
                </form>
            </td>
        </tr>

        <tr>
            <td>
                Napovedi nasprotnika:
            </td>
        </tr>
        <tr>
            <td>
                Uspešne 
            </td>

            <td>
                Tihe
            </td>
        
            <td>
                Neuspešne 
            </td>        
        </tr>
        
        <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="T"> Trula <br>
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="P"> Pagat <br>
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="V"> Valat <br>
                  <input type="checkbox" name="uspešna_napoved_nasprotnik" value="BV"> Barvni Valat
                </form>
            </td>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="tiha_nasprotnik" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="tiha_nasprotnik" value="T"> Trula <br>
                  <input type="checkbox" name="tiha_nasprotnik" value="P"> Pagat <br>
                  <input type="checkbox" name="tiha_nasprotnik" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="tiha_nasprotnik" value="V"> Valat 
                </form>
            </td>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="4K"> Štirje kralji <br>
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="T"> Trula <br>
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="P"> Pagat <br>
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="ZK"> Zadnji kralj <br>
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="V"> Valat <br>
                  <input type="checkbox" name="neuspešna_napoved_nasprotnik" value="BV"> Barvni Valat
                </form>
            </td>
        </tr>

        <tr>
            <td>
                Mond Fang:
            </td>
        </tr>

         <tr>
            <td>
                <form action="/ScoreBoard/racunanje">
                  <input type="radio" name="mond_fang" value="p1"> p1<br>
                  <input type="radio" name="mond_fang" value="p2"> p3<br>
                  <input type="radio" name="mond_fang" value="p3"> p3 <br>
                  <input type="radio" name="mond_fang" value="p4"> p4
                </form>
            </td>
        </tr>
        
        <tr>
            <td>
                <form action="/ScoreBoard/racunanje" method="POST">
                    <input type="submit" value="Dodaj partijo">
                </form>
            </td>
        </tr>

        <tr>
            <td>
                <form action="/test" method="POST">
                    <input type="submit" value="Dodaj partijo">
                </form>
            </td>
        </tr>
    </table>


                

</html>