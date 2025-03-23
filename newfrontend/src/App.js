import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Search from './components/Search';
import Navbar from './components/Navbar';

function App() {
  const myWidth =220

  return (
    <div className="App">
       <Navbar
        drawerWidth={myWidth}
        content = {
          <Routes>
            <Route path="" element ={<Home/>}/>
            <Route path="/about" element ={<About/>}/>
            <Route path="/search" element ={<Search/>}/>
         </Routes>
        }
        
         />

       
    </div>
  );
}

export default App;
