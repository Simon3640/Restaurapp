import { Component, Input, OnInit } from '@angular/core';
import { ProductService } from '@app/shared/services/product.service';
import { Product } from '@app/shared/interfaces/product.interface';
import { Observable, take } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {

  product: any;
  @Input() id: number=0;

  constructor(
    private route:ActivatedRoute,
    private productSvc:ProductService,
    private modal: NgbModal
  ) { }
  ngOnInit(): void {
    this.productSvc.getDetails(this.id).subscribe(
      (res:any) => {
        const result = res;
        this.product = result;
      }
    )
  }

  close(){
      this.modal.dismissAll('reason');
  }
  add(){
    console.log(this.product);
    this.close();
  }
}
