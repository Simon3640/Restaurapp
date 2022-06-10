import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Product } from '@shared/interfaces/product.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  prefix = 'http://localhost:8000/';

  searchProducts(query: string) {
  const filter = this.prefix + 'products/?category=' + query;
  return this.http.get<Product[]>(filter);
  }

  getAllProducts() {
  return this.http.get<Product[]>(this.prefix + 'products');
  }
  getDetails(id: number) {
    return this.http.get<Product>(this.prefix + `product/${id}`);
  }

  postProduct(product: any) {
    const prueba :Product = product;
    const headers = new HttpHeaders();
    headers.set('Content-Type', 'application/json')
    return this.http.post(this.prefix + 'product/new', prueba, {headers: headers});
  
  }

  deleteProduct(id: number) {
    return this.http.delete(this.prefix + `product/delete/${id}`);
  }

}
