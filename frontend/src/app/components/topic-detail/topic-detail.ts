import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-topic-detail',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './topic-detail.html',
  styleUrl: './topic-detail.css'
})
export class TopicDetail implements OnInit {
  topic: any = null;

  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getTopic(id).subscribe(data => {
      this.topic = data;
    });
  }
}
