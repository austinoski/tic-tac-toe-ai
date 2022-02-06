
const app = Vue.createApp({
    data() {
        return {
            board: [
                "[ ]", "[ ]", "[ ]",
                "[ ]", "[ ]", "[ ]",
                "[ ]", "[ ]", "[ ]"
            ],
            turn: 0,
            ai_player_mark: "O",
            human_player_mark: "X",
            empty_cell_mark: "[ ]",
            ai_url: "https://tic-tac-toe-ai-player.herokuapp.com/predict"
        }
    },

    methods: {
        markCell(cell_no){
            if(this.board[cell_no] === this.empty_cell_mark && this.turn === 0){
                this.board[cell_no] = this.human_player_mark
                this.turn = 1
            }
            if(this.turn === 1){
                this.aiPlay()
                this.turn = 0
            }
        },

        aiPlay(){
            let board = [0,0,0,0,0,0,0,0,0]
            for (let i = 0; i < board.length; i++){
                if(this.board[i] === this.ai_player_mark){
                    board[i] = -1
                } else if(this.board[i] === this.human_player_mark){
                    board[i] = 1
                } else{
                    board[i] = 0
                }
            }

            post_data = {
                method: "POST",
                body: JSON.stringify({"board": board}),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            }
            this.getData(this.ai_url, post_data, this.board, this.ai_player_mark)
        },

        getData(url, data, board, mark){
            fetch(url, data)
            .then((response) => response.json())
            .then(function(data){
                board[data["move"]] = mark
            })
            .catch((err) => console.log(err));
        },

        resetGame(){
            board = []
            for (let i = 0; i < 10; i++){
                board.push(this.empty_cell_mark)
            }
            this.board = board
        }
    }
});

app.mount("#app")
