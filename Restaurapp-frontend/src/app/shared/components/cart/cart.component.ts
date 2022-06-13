import { Component, OnInit } from '@angular/core';
import { ProductToCartService } from '@app/shared/services/Connections/product-to-cart.service';
import { ProductService } from '@app/shared/services/product.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { CookieService } from 'ngx-cookie-service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  messageReceived: string = '';
  private sub$!: Subscription;
  ventaInfo : any = [];
  products : any[] = [];

  constructor(
    private cookieSvc: CookieService,
    private productToCart : ProductToCartService,
    private productSvc : ProductService,
    private modal: NgbActiveModal,
  ) {
    // this.subscriptionName = this.productToCart.getUpdate().subscribe
    // (message => {
    //   this.messageReceived = message;
    //   this.ngOnInit();
    // })
   }

  ngOnInit(): void {
    // if (this.cookieSvc.get('cart')) {
    //   this.ventaInfo = JSON.parse(this.cookieSvc.get('cart'));
    //   for (let i = 0; i < this.ventaInfo.length; i++) {
    //     this.productSvc.getDetails(this.ventaInfo[i].id).subscribe(
    //       (res:any) => { 
    //         const result = res;
    //         this.products.push(result);
    //       });
    //     }
    // }
      this.sub$ = this.productToCart.myCart$
      .subscribe(data => {
      this.products = data;
      })
  }

  removeProduct(index: number) {
    this.productToCart.removeProduct(index);
    if (this.products.length === 0) {
      this.onClose();
    }
  }

  onConfirm() {
    console.log(this.products);
    this.modal.close('confirm');

  }

  onClose() {
    this.modal.close('closed');
  }

  ngOnDestroy() {
    this.sub$.unsubscribe();
  }
}
