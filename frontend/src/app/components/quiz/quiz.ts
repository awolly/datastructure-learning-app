import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-quiz',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './quiz.html',
  styleUrl: './quiz.css'
})
export class Quiz implements OnInit {
  topicId: number = 0;
  questions: any[] = [];
  currentQuestion: number = 0;
  selectedAnswer: string = '';
  result: any = null;
  score: number = 0;
  quizComplete: boolean = false;

  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.topicId = Number(this.route.snapshot.paramMap.get('topicId'));
    this.api.getQuiz(this.topicId).subscribe(data => {
      this.questions = data.quiz;
    });
  }

  selectAnswer(option: string) {
    this.selectedAnswer = option;
  }

  submitAnswer() {
    if (!this.selectedAnswer) return;

    const question = this.questions[this.currentQuestion];
    this.api.submitAnswer(this.topicId, question.id, this.selectedAnswer).subscribe(data => {
      this.result = data;
      if (data.correct) {
        this.score++;
      }
    });
  }

  nextQuestion() {
    this.currentQuestion++;
    this.selectedAnswer = '';
    this.result = null;

    if (this.currentQuestion >= this.questions.length) {
      this.quizComplete = true;
    }
  }
}