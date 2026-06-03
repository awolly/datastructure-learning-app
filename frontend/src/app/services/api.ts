import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {}

  getTopics(): Observable<any> {
    return this.http.get(`${this.baseUrl}/topics`);
  }

  getTopic(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/topics/${id}`);
  }

  getLesson(topicId: number, lessonId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/topics/${topicId}/lessons/${lessonId}`);
  }

  getQuiz(topicId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/topics/${topicId}/quiz`);
  }

  submitAnswer(topicId: number, questionId: number, answer: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/topics/${topicId}/quiz/${questionId}/answer`, { answer });
  }
}