# scripts utiles

### javascript :

- Canvas



**dessiner avec la souris**

let ratio = 0.8 ;

function setup() {
  createCanvas(windowWidth*ratio, windowHeight*ratio);
}

function draw() {
  ellipse(mouseX, mouseY, 80, 80);
}



**alerte**

function maFonction() {
	alert("Le JavaScript fonctionne !")
}

<!---
À intégrer dans le html comme ça :
-->

<button onclick="maFonction()">Cliquer ici</button>