import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import AppBar from '@mui/material/AppBar';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import {Link, useLocation} from 'react-router-dom';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import HomeIcon from '@mui/icons-material/Home';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import SearchIcon from '@mui/icons-material/Search';
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';
import ShoppingCartOutlinedIcon from '@mui/icons-material/ShoppingCartOutlined';
import { IconButton } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

export default function Navbar(props) {
    const {drawerWidth, content} = props
    const location =useLocation()
    const path = location.pathname

    const [open, setOpen] = React.useState(false);
    
const changeOpenStatus = () => {
    setOpen(!open)
}

    const myDrawer = (
    <div>
          
<Toolbar />
        <Box sx={{ overflow: 'auto' }}>
          <List>
              <ListItem disablePadding>
                <ListItemButton component={Link} to="/" selected={"/"=== path}>
                  <ListItemIcon>
                    <HomeOutlinedIcon/>
                  </ListItemIcon>
                  <ListItemText primary={"Home"} />
                </ListItemButton>
              </ListItem>

               <ListItem disablePadding>
                <ListItemButton component={Link} to="/about" selected={"/about"=== path}>
                  <ListItemIcon>
                    <InfoOutlinedIcon/>
                  </ListItemIcon>
                  <ListItemText primary={"About"} />
                </ListItemButton>
              </ListItem>

               <ListItem disablePadding>
                <ListItemButton component={Link} to="/search" selected={"/search"=== path}>
                  <ListItemIcon>
                    <SearchIcon/>
                  </ListItemIcon>
                  <ListItemText primary={"Search"} />
                </ListItemButton>
              </ListItem>

              <ListItem disablePadding>
                <ListItemButton component={Link} to="/cart" selected={"/cart"=== path}>
                  <ListItemIcon>
                    <ShoppingCartOutlinedIcon/>
                  </ListItemIcon>
                  <ListItemText primary={"Cart"} />
                </ListItemButton>
              </ListItem>

              <ListItem disablePadding>
                <ListItemButton component={Link} to="/account" selected={"/account"=== path}>
                  <ListItemIcon>
                    <HomeOutlinedIcon/>
                  </ListItemIcon>
                  <ListItemText primary={"Account"} />
                </ListItemButton>
              </ListItem>

          </List>
          <Divider />
          
        </Box>

    </div>

    )

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>

       
           <IconButton
               color ="inheret"
                onClick={changeOpenStatus}
                sx={{me:2,display:{sm:"none"}}}
                >
                     <MenuIcon/>

           </IconButton>
          <Typography variant="h6" noWrap component="div">
            FoodieExpress
          </Typography>
        </Toolbar>
      </AppBar>

        <Drawer
            variant="permanent"
            sx={{
            display: {xs:"none", sm:"block"},
            width: drawerWidth,
            flexShrink: 0,
            [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
            }}
            >
        
            {myDrawer}

      </Drawer>

      <Drawer
            variant="temporary"
            opem ={open}
            onClose = {changeOpenStatus}
            sx={{
            display: {xs:"block", sm:"none"},
            width: drawerWidth,
            flexShrink: 0,
            [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
            }}
            >
        
            {myDrawer}

      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        
            {content}

      </Box>
    </Box>
  );
}
