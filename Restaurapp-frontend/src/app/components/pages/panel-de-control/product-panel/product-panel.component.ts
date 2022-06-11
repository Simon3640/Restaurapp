import { Component, OnInit } from '@angular/core';
import { Product } from '@app/shared/interfaces/product.interface';
import { ProductService } from '@app/shared/services/product.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { EditProductComponent } from '../edit-product/edit-product.component';
import { NewProductModule } from '../new-product/new-product.module';

@Component({
  selector: 'app-product-panel',
  templateUrl: './product-panel.component.html',
  styleUrls: ['./product-panel.component.scss']
})
export class ProductPanelComponent implements OnInit {

  constructor(
    private productSvc: ProductService,
    private modal: NgbModal
    ) { }
  
  
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

  delProduct(id: any): void {
    if (confirm('¿Estás seguro de eliminar este producto?')) {
    this.productSvc.deleteProduct(id)
    .subscribe(
      data => {
        this.ngOnInit();
      }),
      () => {
        console.log('Error occured');
      }
    
    }
  }
  
  openNewProduct() {
    const modalRef = this.modal.open(NewProductModule); 
  }

  openSM(productid: any) {
    const modalRef = this.modal.open(EditProductComponent);
    modalRef.componentInstance.id = productid;
    modalRef.result.then((result) => {
      if ( result === 'success' ) {
         this.ngOnInit(); // Refresh Data in table grid
      }
    }, (reason) => {
    });

  }
}
