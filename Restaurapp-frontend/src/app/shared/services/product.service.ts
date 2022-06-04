import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Product } from '@shared/interfaces/product.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  searchProducts(query: string) {
  const filter = 'http://localhost:8000/products/?category=' + query;
  return this.http.get<Product[]>(filter);
  }
  getDetails(id: number) {
    return this.http.get<Product>(`http://localhost:8000/product/${id}`);
  }
}
