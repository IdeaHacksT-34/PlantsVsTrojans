let s_width = 1000, s_height = 600;
let person, philip, jessica, andrea, eric, buttons;
let small_icon, heart_img, game_over_text, main_background, main_menu_background, htp_background, about_bg, golden_border;
let char_x, char_y;
let startBtn, xBtn, htpBtn;
let bg_song;
let index, characters;
let startGameBtn;
let obj;
let fallingObjects;
let catch_obj;
let lives, score;
let gameover;
let border_coords;
let chosen_char;
let pick_eric, pick_jessica, pick_andrea, pick_philip;
let song_play;
let mode = 1;

function preload() {
	// Sounds
	bg_song = loadSound("Game Files/Sounds/background_song.mp3");
	hit_sound = loadSound("Game Files/Sounds/270326__littlerobotsoundfactory__hit-01.wav");
	pickup_sound = loadSound("Game Files/Sounds/347172__davidsraba__coin-pickup-sound.wav");
	gameover_sound = loadSound("Game Files/Sounds/253886__themusicalnomad__negative-beeps.wav")
	// Font
	custom_font = loadFont('Game Files/Fonts/fipps.otf');
	// Other Images
	small_icon = loadImage('Game Files/Images/Etc/small_icon.png');
	heart_img = loadImage('Game Files/Images/Etc/heart.png');
	game_over_text = loadImage('Game Files/Images/Etc/gameover.png');
	main_background = loadImage('Game Files/Images/Backgrounds/char_select.png');
	main_menu_background = loadImage('Game Files/Images/Backgrounds/main_menu_bg.png');
	htp_background = loadImage('Game Files/Images/Backgrounds/htp.png');
	about_bg = loadImage('Game Files/Images/Backgrounds/about.png');
	golden_border = loadImage('Game Files/Images/Borders/gold_border.png');
	philip = {
		background: loadImage('Game Files/Images/Backgrounds/philip_bg.png'),
		char: loadImage('Game Files/Images/Leads/philip.png'),
		obstacle: loadImage('Game Files/Images/Obstacles/philip_obstacle.png'),
		catch: loadImage('Game Files/Images/Catch/philip_catch.png'),
		inactive: loadImage('Game Files/Images/Borders/philip_border_inactive.png'),
		active: loadImage('Game Files/Images/Borders/philip_border_active.png')
	};
	jessica = {
		background: loadImage('Game Files/Images/Backgrounds/jessica_bg.png'),
		char: loadImage('Game Files/Images/Leads/jessica.png'),
		obstacle: loadImage('Game Files/Images/Obstacles/jessica_obstacle.png'),
		catch: loadImage('Game Files/Images/Catch/jessica_catch.png'),
		inactive: loadImage('Game Files/Images/Borders/jessica_border_inactive.png'),
		active: loadImage('Game Files/Images/Borders/jessica_border_active.png')
	};
	andrea = {
		background: loadImage('Game Files/Images/Backgrounds/andrea_bg.png'),
		char: loadImage('Game Files/Images/Leads/andrea.png'),
		obstacle: loadImage('Game Files/Images/Obstacles/andrea_obstacle.png'),
		catch: loadImage('Game Files/Images/Catch/andrea_catch.png'),
		inactive: loadImage('Game Files/Images/Borders/andrea_border_inactive.png'),
		active: loadImage('Game Files/Images/Borders/andrea_border_active.png')
	};
	eric = {
		background: loadImage('Game Files/Images/Backgrounds/eric_bg.png'),
		char: loadImage('Game Files/Images/Leads/eric.png'),
		obstacle: loadImage('Game Files/Images/Obstacles/eric_obstacle.png'),
		catch: loadImage('Game Files/Images/Catch/eric_catch.png'),
		inactive: loadImage('Game Files/Images/Borders/eric_border_inactive.png'),
		active: loadImage('Game Files/Images/Borders/eric_border_active.png')
	};
	buttons = {
		play_again: [loadImage('Game Files/Buttons/play_again_inactive.png'), loadImage('Game Files/Buttons/play_again_active.png')],
		quit: [loadImage('Game Files/Buttons/quit_inactive.png'), loadImage('Game Files/Buttons/quit_active.png')],
		menu: [loadImage('Game Files/Buttons/menu_inactive.png'), loadImage('Game Files/Buttons/menu_active.png')],
		start: [loadImage('Game Files/Buttons/start_inactive.png'), loadImage('Game Files/Buttons/start_active.png'), loadImage('Game Files/Buttons/start_disabled.png')],
		main_start: [loadImage('Game Files/Buttons/main_start_inactive.png'), loadImage('Game Files/Buttons/main_start_active.png')],
		htp: [loadImage('Game Files/Buttons/htp_inactive.png'), loadImage('Game Files/Buttons/htp_active.png')],
		about: [loadImage('Game Files/Buttons/about_inactive.png'), loadImage('Game Files/Buttons/about_active.png')],
		back: [loadImage('Game Files/Buttons/cancel_inactive.png'), loadImage('Game Files/Buttons/cancel_active.png')]
	};

}

function initializeObjects() {
	let numObjects = 4;
  	fallingObjects = [];
  	for (let k=0; k<numObjects; k++) {
  		let x = random(s_width-(person.obstacle.width));
  		let y = -person.obstacle.height;
  		let speed = random(5,10);
  		fallingObjects[k] = new FallingObject(x, y, speed, person.obstacle, "obstacle");
  	}
  	catch_obj = new FallingObject(random(s_width-(person.catch.width)), -random(person.catch.height+200), random(5,10), person.catch, "catch");
}

function setup() {
  	createCanvas(s_width, s_height);
  	textFont(custom_font);
  	textSize(40);
  	chosen_char = false;
  	person = null;
  	bg_song.setVolume(0.10);
  	song_play = false;
  	gameover_sound.setVolume(0.40);
  	pickup_sound.setVolume(0.18);
  	hit_sound.setVolume(0.15);
}

function draw() {
	if (mode == 0) {
		game();
	}
	else if (mode == 1) {
		mainMenu();
	}
	else if (mode == 2) {
		htpPage();
	}
	else if (mode == 3) {
		aboutPage();
	}
	else if (mode == 4) {
		crash();
	}
	else if (mode == 5) {
		charSelect();
	}
}


function resetGame() {
	score = 0;
	lives = 3;
	gameover = false;
	char_x = (s_width-person.char.width)/2;
  	char_y = s_height-person.char.height;
  	initializeObjects();
}


function charSelect() {
	image(main_background, 0, 0);
	pick_eric = new customButton(eric.inactive, eric.active, 20, 100);
	pick_jessica = new customButton(jessica.inactive, jessica.active, 265, 100);
	pick_andrea = new customButton(andrea.inactive, andrea.active, 510, 100);
	pick_philip = new customButton(philip.inactive, philip.active, 755, 100);

	if (chosen_char == true) {
		startGameBtn = new customButton(buttons.start[0], buttons.start[1], 377, 510);
	}
	else {
		startDisabled = new customButton(buttons.start[2], buttons.start[2], 377, 510);
	}
}


function htpPage() {
	image(htp_background, 0, 0,);
	xBtn = new customButton(buttons.back[0], buttons.back[1], 20, 20);
}


function aboutPage() {
	image(about_bg, 0, 0);
	xBtn = new customButton(buttons.back[0], buttons.back[1], 20, 20);
}


let playAgainBtn, mainMenuBtn;
function mouseClicked() {
	if (song_play == false && mouseX > 0 && mouseX < s_width && mouseY > 0 && mouseY < s_height) {
		song_play = true;
		bg_song.loop();
	}
	if (mode == 1) {
		aboutBtn.clicked(mouseX, mouseY, "about");
		startBtn.clicked(mouseX, mouseY, "charSelect");
		htpBtn.clicked(mouseX, mouseY, "htp");
	}
	if (mode == 3 || mode == 2) {
		xBtn.clicked(mouseX, mouseY, "mainMenu");
	}
	if (mode == 4) {
		playAgainBtn.clicked(mouseX, mouseY, "reset");
		mainMenuBtn.clicked(mouseX, mouseY, "mainMenu");
	}
	if (mode == 5) {
		pick_eric.clicked(mouseX, mouseY, "eric");
		pick_jessica.clicked(mouseX, mouseY, "jessica");
		pick_andrea.clicked(mouseX, mouseY, "andrea");
		pick_philip.clicked(mouseX, mouseY, "philip");
		if (chosen_char == true) {
			startGameBtn.clicked(mouseX, mouseY, "play");
		}
	}
}

function reset_char_select() {
	person = null;
	chosen_char = false;
}

function set_char(character) {
	person = character;
	chosen_char = true;
}

class customButton {
	constructor(inactive, active, x, y) {

		this.inactive = inactive;
		this.active = active;
		this.x = x;
		this.y = y;
		let button_h = this.inactive.height;
		let button_w = this.active.width;
		if ((this.x < mouseX && mouseX < this.x + button_w) && (this.y < mouseY && mouseY < this.y + button_h)) {
			image(this.active, this.x, this.y);
		}
		else {
			image(this.inactive, this.x, this.y);
		}
		if (person != null && mode == 5) {
			image(golden_border, border_coords[0], border_coords[1]);
		}
	}
	clicked(mx, my, action) {
		let button_h = this.inactive.height;
		let button_w = this.active.width;
		if ((this.x < mx && mx < this.x + button_w) && (this.y < my && my < this.y + button_h)) {
			if (action == "game" && mode == 1) {
				resetGame();
				initializeObjects();
				mode = 0;
			}
			else if (action == "htp" && mode == 1) {
				mode = 2;
			}
			else if (action == "mainMenu") {

				reset_char_select();
				
				mode = 1;
			}
			else if (action == "about") {
				mode = 3;

			}
			else if (action == "gameover") {
				mode = 4;
			}
			else if (action == "reset" && mode == 4) {
				resetGame();
				initializeObjects();
				mode = 0;
			}
			else if (action == "charSelect") {
				mode = 5;
			}
			else if (action == "eric" && mode == 5) {
				set_char(eric);
				border_coords = [20, 100];
			}
			else if (action == "jessica") {
				set_char(jessica);
				border_coords = [265, 100];
			}
			else if (action == "andrea") {
				set_char(andrea);
				border_coords = [510, 100];
			}
			else if (action == "philip") {
				set_char(philip);
				border_coords = [755, 100];
			}
			else if (action == "play" && mode == 5) {
				resetGame();
				initializeObjects();
				mode = 0;
			}
		}
	}
}

function mainMenu() {
	image(main_menu_background, 0, 0);
	startBtn = new customButton(buttons.main_start[0], buttons.main_start[1], 250, 220);
	htpBtn = new customButton(buttons.htp[0], buttons.htp[1], 250, 320);
	aboutBtn = new customButton(buttons.about[0], buttons.about[1], 250, 420);
}

function crash() {
	image(game_over_text, 0, 100);
	playAgainBtn = new customButton(buttons.play_again[0], buttons.play_again[1], 330, 280);
	mainMenuBtn = new customButton(buttons.menu[0], buttons.menu[1], 330, 380);

}

function game() {
	if (gameover == false) {
		image(person.background, 0, 0);
		let char_speed = 15;
		image(person.char, char_x, char_y);
		if ((keyIsDown(LEFT_ARROW) || keyIsDown(65)) && char_x > 0) {
			char_x -= char_speed;
		}
		if ((keyIsDown(RIGHT_ARROW) || keyIsDown(68)) && (char_x+person.char.width) < s_width) {
			char_x += char_speed;
		}

		for (let i=0; i<fallingObjects.length; i++) {
			fallingObjects[i].move();
			fallingObjects[i].show();
		}

		catch_obj.move();
		catch_obj.show();

		draw_hearts();
		text(score, s_width/2, 90);
	}
}

function draw_hearts() {
	let tmp = 55;
	for (let i=0; i<lives; i++) {
		image(heart_img, s_width-tmp, 5);
		tmp += 55;
	}
}


class FallingObject {
	constructor(x, y, speed, object_img, type) {
		this.x = x;
		this.y = y;
		this.speed = speed;
		this.object_img = object_img;
		this.type = type;
	}
	reinit() {
		this.y = -this.object_img.height;
		this.x = random(s_width-this.object_img.width);
		this.speed = random(5,10);
	}
	move() {
		this.y += this.speed;
		if (this.y > s_height) {
			this.reinit();
		}
		if (char_y < this.y+30) {
			if (char_x <= this.x && this.x <= char_x + person.char.width || char_x <= this.x + this.object_img.width && this.x + this.object_img.width <= char_x + person.char.width) {
				if (this.type == "obstacle") {
					hit_sound.play();
					if (lives > 1) {
						lives -= 1;
					}
					else {
						lives -= 1;
						gameover = true;
						gameover_sound.play();
						mode = 4;
					}
				}
				else if (this.type == "catch") {
					score++; 
					pickup_sound.play();
				}
				this.reinit();
			}
		}
	}
	show() {
		image(this.object_img, this.x, this.y);
	}
}