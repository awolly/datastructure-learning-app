import { Routes } from '@angular/router';
import { TopicList } from './components/topic-list/topic-list';
import { TopicDetail } from './components/topic-detail/topic-detail';
import { Lesson} from './components/lesson/lesson';
import { Quiz } from './components/quiz/quiz';

export const routes: Routes = [
  { path: '', component: TopicList },
  { path: 'topics/:id', component: TopicDetail },
  { path: 'topics/:topicId/lessons/:lessonId', component: Lesson },
  { path: 'topics/:topicId/quiz', component: Quiz }
];