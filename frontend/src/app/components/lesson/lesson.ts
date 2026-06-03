import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-lesson',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './lesson.html',
  styleUrl: './lesson.css'
})
export class Lesson implements OnInit {
  lesson: any = null;
  topicId: number = 0;

  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.topicId = Number(this.route.snapshot.paramMap.get('topicId'));
    const lessonId = Number(this.route.snapshot.paramMap.get('lessonId'));
    this.api.getLesson(this.topicId, lessonId).subscribe(data => {
      this.lesson = data;
    });
  }
}
