import { Component, HostListener } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CartComponent } from './shared/components/cart/cart.component';
import { Subscription } from 'rxjs';
import { ProductToCartService } from './shared/services/Connections/product-to-cart.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Restaurapp';
  productInCart = false;
  messageReceived: string = '';
  nProducts : number = 0;
  total = 0;
  private sub$!: Subscription;
  constructor(
    private cookieSvc: CookieService,
    private modal : NgbModal,
    private productToCart : ProductToCartService
    ) { 
  }

  ngOnInit() {
    this.productToCart.getFromCookie();
    this.productToCart.myCart$
    .subscribe(data => {
      this.total = data.reduce((acc, cur) => {
        return acc + cur.Value;
      },0);
      this.nProducts = data.length;
      this.productInCart = data.length > 0 ? true : false;
    })
  }
  
  open(){
    this.modal.open(CartComponent);
  }
  
  ngOnDestroy() {
    this.sub$.unsubscribe();
  }
}
