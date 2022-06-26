import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Category } from '../interfaces/category.interface';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor(private http: HttpClient) { }

  prefix= 'http://localhost:8000/';
  getCategories(){
    return this.http.get<Category[]>(this.prefix+'categories');
  }

  postCategory(category: Category) {
    const prueba :Category = category;
    const headers = new HttpHeaders();
    headers.set('Content-Type', 'application/json')
    return this.http.post<Category>(this.prefix+'category/new', prueba, {headers: headers});
  }


}
