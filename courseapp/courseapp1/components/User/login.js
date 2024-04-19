import { TouchableOpacity, View } from "react-native"
import Mystyle from  "../../Style/Mystyle"
import Style from "./Style";
import { TextInput } from "react-native-gesture-handler"
const login = () => {
    return 
    (
        <View style={Mystyle}>
            <text>login</text>
        
            <TouchableOpacity>
                <Text style= {Style.button}>Login</Text>
            </TouchableOpacity>
        </View>
    )
}
export default login;