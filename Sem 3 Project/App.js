import React from "react";
import {BrowserRouter as Router, Route, Routes, Link} from "react-router-dom";
// import Home from "./home";
// import About from "./about";
import OsuChildren from "./Osu_Children"
import StyledLink from "./style";
const express = require('express');
const app = express();
app.use(express.static('public'));
app.listen(3000, () => {
    console.log("Example app listening on port http://localhost:3000/Osu-Children.html");
});
class App extends React.Component{
    render(){
        return(
            <Router>
                <Link>
                    {/* <div><StyledLink to = "/">Home</StyledLink></div>
                    <div><StyledLink to = "/about">Songs</StyledLink></div> */}
                    <div><StyledLink to = "/Osu_Children">Arya's Game</StyledLink></div>
                </Link>
                <Routes>
                    {/* <Route exact path = "/" element = {<Home/>}/>
                    <Route path = "/about" element = {<About/>}/> */}
                    <Route path = "/Osu_Children" element = {<OsuChildren/>}/>
                </Routes> 
            </Router>
        )
    }
}
export default App;