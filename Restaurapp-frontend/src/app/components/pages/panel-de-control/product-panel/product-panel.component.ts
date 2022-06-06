import { Component, OnInit } from '@angular/core';
import { Product } from '@app/shared/interfaces/product.interface';
import { ProductService } from '@app/shared/services/product.service';

@Component({
  selector: 'app-product-panel',
  templateUrl: './product-panel.component.html',
  styleUrls: ['./product-panel.component.scss']
})
export class ProductPanelComponent implements OnInit {

  constructor(private productSvc: ProductService) { }
  products: Product[] = [];
  ngOnInit(): void {
    this.getDataFromService();
  }

  private getDataFromService(): void {
    this.productSvc.getAllProducts().subscribe((res:any) => {
      const results = res;
      this.products = results
    });
  }


}
