import { Component, OnInit } from '@angular/core';
import { ProductService } from '@app/shared/services/product.service';
import { Product } from '@app/shared/interfaces/product.interface';
import { Observable, take } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {

  product$: Observable<Product> | undefined;

  constructor(private route:ActivatedRoute, private productSvc:ProductService) { }

  ngOnInit(): void {

    this.route.params.pipe(take(1)).subscribe((params) => {
      const id = params['id'];
      this.product$ = this.productSvc.getDetails(id);
    });
  }

}
