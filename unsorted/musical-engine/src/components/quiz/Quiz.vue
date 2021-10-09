<template>
    <div id="quiz-container">
<div v-if="currentQuestion.questionType ==='multiple_choice'">
<div class="w3-left-align">{{currentQuestion.question}}</div>
<div class="w3-row">
    <div class="w3-col m12"> <span style="float: left;" class="w3-left-align">A.</span><button class="w3-left-align w3-btn" style="float:left;" @click="updateAnswer" id="currentQuestion.choices[0]">{{currentQuestion.choices[0]}}</button></div>
    <div class="w3-col m12"> <span style="float: left;" class="w3-left-align">B.</span><button class="w3-left-align w3-btn" style="float:left;" @click="updateAnswer" id="currentQuestion.choices[1]">{{currentQuestion.choices[1]}}</button></div>
    <div class="w3-col m12"> <span style="float: left;" class="w3-left-align">C.</span><button class="w3-left-align w3-btn" style="float:left;" @click="updateAnswer" id="currentQuestion.choices[2]">{{currentQuestion.choices[2]}}</button></div>
    <div class="w3-col m12"> <span style="float: left;" class="w3-left-align">D.</span><button class="w3-left-align w3-btn" style="float:left;" @click="updateAnswer" id="currentQuestion.choices[3]">{{currentQuestion.choices[3]}}</button></div>
</div>
</div>
    </div>
</template>

<script>
    export default {
    name: 'Quiz',
    methods:{
        nextQuestion() {

        },
        updateAnswer(){
            // this.userAnswers
        },
    },
    computed: {
        multipleChoices () {},
        shortAnswer () {},
        trueOrFalse () {},
        currentQuestion(){
            if (this.quizData!==[])return this.quizData[this.renderedQuestion-1]
            return null
        },
        totalQuestions(){
            return this.quizData.length
        }
    },
    data(){
        return {
            loading: true,
            selection:"",
            renderedQuestion:1,
            userAnswers:[

            ],
            quizData:[
                // https://www.theguardian.com/tv-and-radio/ng-interactive/2020/sep/12/who-wants-to-be-a-millionaire-jackpot-questions-quiz-yourself
                {
                    id:1,
                question:"In the UK, the abbreviation NHS stands for National what Service?",                
                choices:['Humanity', 'Health', 'Honour','Household'],
                correctAnswer:'Health',
                questionType:"multiple_choice"
                },
                {id:2,
                    question:"Which Disney character famously leaves a glass slipper behind at a royal ball?",
                    choices:['Pocahontas','Sleeping Beauty','Cinderella','Elsa'],
                    correctAnswer:'Cinderella',
                    questionType:"multiple_choice"
                },
                {
                    id:3,
                    question:"What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?",
                }
            ]
        }
    }
    }
</script>

<style scoped>

</style>