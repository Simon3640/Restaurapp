import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { BehaviorSubject } from 'rxjs';
import { ProductService } from '../product.service';

@Injectable({
  providedIn: 'root'
})
export class ProductToCartService {
  private Cart : any[] = [];
  private myCart = new BehaviorSubject<any[]>([]);
  public myCart$ = this.myCart.asObservable();
  
  constructor(
    private productSvc: ProductService,
    private cookieSvc: CookieService,
    )
  {
    
  }
  getFromCookie() {
    if(this.cookieSvc.check('cart'))
    {
      const psProduct = JSON.parse(this.cookieSvc.get('cart'));
      for(let i = 0; i < psProduct.length; i++){
        this.productSvc.getDetails(psProduct[i].id).subscribe(
          (res:any) => { 
            const result = res;
            this.Cart.push(result);
            this.myCart.next(this.Cart);
          });
      }
    }
  }
  
  addProduct(product: any) {
    this.Cart.push(product);
    this.myCart.next(this.Cart);
    if (this.cookieSvc.check('cart')) {
      this.cookieSvc.delete('cart');
    }
    const psProducts = [];
    for(let product of this.Cart){
      psProducts.push({id: product.id, ingredients: product.ingredients});
    }
    this.cookieSvc.set('cart', JSON.stringify(psProducts));
  }

  removeProduct(index: number) {
    this.Cart.splice(index, 1);
    this.myCart.next(this.Cart);
    if (this.cookieSvc.check('cart')) {
      this.cookieSvc.delete('cart');
    }
    const psProducts = [];
    for(let product of this.Cart){
      psProducts.push({id: product.id, ingredients: product.ingredients});
    }
    this.Cart.length === 0 ? this.cookieSvc.delete('cart') : 
    this.cookieSvc.set('cart', JSON.stringify(psProducts));
  }

}

