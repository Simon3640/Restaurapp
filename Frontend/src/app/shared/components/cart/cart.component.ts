import { Component, OnInit } from '@angular/core';
import { Product } from '@app/shared/interfaces/product.interface';
import { ProductToCartService } from '@app/shared/services/Connections/product-to-cart.service';
import { ProductService } from '@app/shared/services/product.service';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CookieService } from 'ngx-cookie-service';
import { Subscription } from 'rxjs';
import { ThxComponent } from './thx/thx.component';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  messageReceived: string = '';
  private sub$!: Subscription;
  ventaInfo : any = [];
  products : Product[] = [];
  total: number = 0;
  edit = Array(this.products.length).fill(false);
  public isCollapsed = false;

  constructor(
    private cookieSvc: CookieService,
    private productToCart : ProductToCartService,
    private productSvc : ProductService,
    private modal: NgbActiveModal,
    private modalr : NgbModal
  ) {
   }

  ngOnInit(): void {
      this.sub$ = this.productToCart.myCart$
      .subscribe(data => {
      this.products = data;
      this.total = this.productToCart.getTotal();
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
    this.productToCart.removeAll();
    this.modal.close('confirm');
    const modalRef = this.modalr.open(ThxComponent);
    return modalRef.result;
  }

  onClose() {
    this.modal.close('closed');
  }

  ngOnDestroy() {
    this.sub$.unsubscribe();
  }
  toggleEdit(index: number) {
    this.edit[index]= !this.edit[index];
  }
}
