import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Product } from '@app/shared/interfaces/product.interface';
import { ProductService } from '@app/shared/services/product.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Observable, take } from 'rxjs';
import { ProductDetailsComponent } from '../product-details/product-details.component';


@Component({
  selector: 'app-products-list',
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.scss']
})
export class ProductsListComponent implements OnInit {
  products$: Observable<Product[]> | undefined;

  private hideScrollHeight = 200;
  private showScrollHeight = 500;





  constructor(private productSvc: ProductService, private modal: NgbModal, private route:ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.pipe(take(1)).subscribe((params) => {
      const id = params['id'];
      this.products$ = this.productSvc.searchProducts(id);
    });
  }


  // private getDataFromService(): void {
  //   this.productSvc.searchProducts(this.query).subscribe((res:any) => {
  //     const results = res;
  //     this.products$ = results
  //   });
  // }
  openSM() {
    this.modal.open(ProductDetailsComponent);
  }
}
