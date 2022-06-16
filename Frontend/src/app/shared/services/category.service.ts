import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Category } from '../interfaces/category.interface';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor(private http: HttpClient) { }

  getCategories(){
    return this.http.get<Category[]>('http://localhost:8000/categories');
  }

  postCategory(category: Category) {
    const prueba :Category = category;
    const headers = new HttpHeaders();
    headers.set('Content-Type', 'application/json')
    return this.http.post<Category>('http://localhost:8000/category/new', prueba, {headers: headers});
  }


}
