import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
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

  getAllProducts() {
  return this.http.get<Product[]>('http://localhost:8000/products');
  }
  getDetails(id: number) {
    return this.http.get<Product>(`http://localhost:8000/product/${id}`);
  }

  postProduct(product: any) {
    const prueba :Product = product;
    const headers = new HttpHeaders();
    headers.set('Content-Type', 'application/json')
    return this.http.post('http://localhost:8000/product/new', prueba, {headers: headers});
  
  }
}
