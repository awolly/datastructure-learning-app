import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-topic-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './topic-list.html',
  styleUrl: './topic-list.css'
})
export class TopicList implements OnInit {
  topics: any[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getTopics().subscribe(data => {
      this.topics = data.topics;
    });
  }
}