import React from "react";
import {Child} from "./Link.js";
class OsuChildren extends React.Component{
    render(){
        Child();
        return(
            <div>
                <a href="http://localhost:3001/Osu-Children.html"><button style="font-size:40px; width:200px">Play Osu:Children</button></a>
                {/* <p>
                    1. Click on the randomly appearing circles to increase your score.<br/>
                    2. Every circle clicked increases the score by 50 and a new circle will appear in a random place on the screen.<br/>
                    3. If you are not able to click a circle within a particular time limit, it will disappear and a new one will appear in a random place. There will be no increase in the score.<br/>
                    4. This will keep going on until the song is over, at which point the game will end.<br/>
                    5. You can pause the game by clicking the pause button when needed, and play it again by clicking the same button.
                </p> */}
                {/* <img src="Screenshot.png" style="height:400px; width:800px" /><br/><br/>
                <a href="Osu-Children.html">
                    <button style="font-size:40px; width:200px">Play</button>
                </a> */}
            </div>
        )
    }
}
export default OsuChildren;