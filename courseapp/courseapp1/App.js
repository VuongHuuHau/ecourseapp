
import { createDrawerNavigator } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native"; 
import login from './components/User/login';
import Home from './components/Home/Home';


const Drawer = createDrawerNavigator();
const App= ()=> {
  return (
    <NavigationContainer>
    <Drawer.Navigator>
    <Drawer.Screen name="Home"component={Home} />
    <Drawer.Screen name="login"component={login} />
    </Drawer.Navigator>
    </NavigationContainer>
  );
}
export default App;
