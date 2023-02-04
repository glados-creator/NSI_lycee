/// get canvas

var canvas = document.getElementById('can_screen');
var can_screen = canvas.getContext('2d');
var can_width = canvas.width;
var can_height = canvas.height;
var can_screen_buffer = new Array(); /// => [ ("img" , img_element_form_to_draw, x , y) , ("line" , ...) , ("text" , ...) ]
can_screen.font = '50px serif';

/// i need the file "type.json" on the server but i don,'t care about the require api
///var data = require('./type.json');
/// so funky function i found on stack-overflow

function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200) {
      result = xmlhttp.responseText;
    }
    return result;
}
/// load database
var data = JSON.parse(loadFile("type.json"));
const can_list = document.getElementById("can_list");
const can_objs = [];
var place = 0;
var select = 0;
var offset_x = 0;
var offset_y = 0;

/// load images in array
var imgs = new Array();
var collection = document.getElementById("img_collect").children
for (let i = 0; i < collection.length; i++) {
    imgs.push([collection[i].children[0].id , collection[i].children[0]]);
    collection[i].children[0].onclick = function ()
    {
        for (let k = 0;k < collection.length;k++) {collection[k].children[0].style.backgroundColor = "#ffffff"}
        place = data.findIndex((x) => x["icon"] == collection[i].children[0].id); 
        this.style.background = "#5050ff";
};
}

function update_select(){
    for (let k = 0;k < can_list.children.length;k++) {can_list.children[k].children[0].style.backgroundColor = "#ffffff"}
        can_list.children[select].children[0].style.background = "#5050ff";
};

function add_obj(x,y){
    if (place == 0) { return;};
    let temp_obj = data[place.toString()];
    let obj = JSON.parse(JSON.stringify(temp_obj));
    let len_list = can_list.children.length;
    obj["index"] = len_list;
    obj["x"] = x + offset_x - 35; /// need to calculate img width and hieght but will do for now
    obj["y"] = y + offset_y - 35;
    let inside = document.createElement("li");
    let text = document.createElement("h3");
    text.textContent = obj["index"] + ". " + obj["name"];
    text.onclick = function txtclick(e) {
        select = obj["index"];
        update_select();
    }
    inside.appendChild(text);
    can_list.appendChild(inside);
    can_objs.push(obj);
};

function flip(mouse_x,mouse_y){
    /// redraw everything for change
    add_obj(mouse_x,mouse_y);
    /// post treament
    can_screen_buffer = [];

    for (let i = 0; i < can_objs.length;i++){
        can_screen_buffer.push(["img",[can_objs[i]["icon"],can_objs[i]["x"] - offset_x,can_objs[i]["y"] - offset_y]]);
    }

    can_screen.fillStyle = "white"; 
    can_screen.fillRect(0,0,can_width,can_height);
    for (let i = 0; i < can_screen_buffer.length; i++) {
        let element = can_screen_buffer[i];
        if (element[0] == "img"){can_screen.drawImage(imgs[imgs.findIndex(x => x[0] == element[1][0])][1], element[1][1],element[1][2]);}
        else if (element[0] == "text"){can_screen.fillText(element[1][0],element[1][1],element[1][2]);}
        else if (element[0] == "line"){
            can_screen.beginPath();
            can_screen.moveTo(element[1][0], element[1][1]);
            can_screen.lineTo(element[1][2], element[1][3]);
            can_screen.stroke();
            can_screen.closePath();}
        else if (element[0] == "dash"){
            can_screen.setLineDash([5,15]);
            can_screen.beginPath();
            can_screen.moveTo(element[1][0], element[1][1]);
            can_screen.lineTo(element[1][2], element[1][3]);
            can_screen.stroke();
            can_screen.closePath();
            can_screen.setLineDash([]);}
        else {console.log(element);console.log("unknown");}
    }
    can_screen.drawImage(imgs[imgs.findIndex(x => x[0] == "images/icon_click.png")][1], mouse_x-35,mouse_y-35);
    return 0;
}

canvas.onclick = function clickEvent(e) {
    // e = Mouse click event.
    var rect = canvas.getBoundingClientRect();
    var mouse_x = e.clientX - rect.left; //x position within the element.
    var mouse_y = e.clientY - rect.top;  //y position within the element.
    /// console.log("Left? : " + mouse_x + " ; Top? : " + mouse_y + ".");
    flip(mouse_x,mouse_y);
}