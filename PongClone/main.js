namespace SpriteKind{

    export const Ball = SpriteKind.create()
} 

let myBall: Sprite = null
let rightPaddle: Sprite = null
let leftPaddle: Sprite =  null

function createLeftPaddle(){
    leftPaddle = sprites.create(assets.image`redPaddleImage`, SpriteKind.Player)
    leftPaddle.setPosition(10, 60)
    leftPaddle.setStayInScreen(true)
    controller.player1.moveSprite(leftPaddle, 0, 100)
    info.player1.setScore(0)
} //defining a function to make the left paddle, put in place and set its motion to a controller

function createRightPaddle(){
    rightPaddle = sprites.create(assets.image`bluePaddleImage`, SpriteKind.Player) //size approx 4x16, blue
    rightPaddle.setPosition(150,60)
    rightPaddle.setStayInScreen(true)
    controller.player2.moveSprite(rightPaddle, 0, 100) //control up and down with the "i" and "k" keys
    info.player2.setScore(0)
} //defining a function to make the right paddle, put it in place, and sets its motion to the controller

function createBall(){
    myBall = sprites.create(assets.image`myBallImage`, SpriteKind.Ball)
    myBall.setVelocity(60,30)
    myBall.setStayInScreen(true)
    myBall.setBounceOnWall(true)
} //creates the ball and sets it to move

sprites.onOverlap(SpriteKind.Ball, SpriteKind.Player, function(sprite: Sprite, otherSprite: Sprite){
    sprite.setVelocity(-sprite.vx, sprite.vy)


    if(otherSprite == leftPaddle){              //if else statement so that ball hits the paddle in the right way + score changes depending on which player hits the ball
        sprite.left = otherSprite.right
    info.player1.changeScoreBy(1)}
    else{
        sprite.right = otherSprite.left
        info.player2.changeScoreBy(1)}
    
}) //what happens if ball hits the paddle 

createLeftPaddle() // "calling" the function to make its code actually run
createRightPaddle() //calling the function defined above
createBall() //calling the function we're defining above 


