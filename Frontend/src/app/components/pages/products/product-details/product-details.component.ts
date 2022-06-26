import { Component, Input, OnInit } from '@angular/core';
import { ProductService } from '@app/shared/services/product.service';

import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

import { ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CookieService } from 'ngx-cookie-service';
import { ProductToCartService } from '@app/shared/services/Connections/product-to-cart.service';
@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {

  product: any;
  totalAdiciones =0;
  ing : string[] = [];
  form : FormGroup;
  form2: FormGroup;
  Adiciones : any[] = [
    {
      name: 'Tocineta',
      price: '1000',
    },
    {
      name: 'Queso chedar',
      price: '2000',
    },
    {
      name: 'Bombón de pollo',
      price: '3000',
    }
  ];
  @Input() id: number=0;

  constructor(
    private route:ActivatedRoute,
    private productSvc:ProductService,
    private modal: NgbModal,
    private fb: FormBuilder,
    private cookieSvc:CookieService,
    private productToCart : ProductToCartService,
  ) { 
    this.form = this.fb.group({
      checkArray: this.fb.array([]),
    });

    this.form2 = this.fb.group({
      checkArray2: this.fb.array([]),
    });

  }
  
  
  submitForm() {
    console.log(this.form.value);
  }
  
  ngOnInit(): void {
    this.productSvc.getDetails(this.id).subscribe(
      (res:any) => {
        const result = res;
        this.product = result;
      }
    )
  }

  onCheckboxChange(e: any) {
    const checkArray: FormArray = this.form.get('checkArray') as FormArray;
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: any) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  onCheckboxChange2(e: any) {
    const checkArray2: FormArray = this.form2.get('checkArray2') as FormArray;
    if (e.target.checked) {
      checkArray2.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray2.controls.forEach((item: any) => {
        if (item.value == e.target.value) {
          checkArray2.removeAt(i);
          return;
        }
        i++;
      });
    }
    this.totalAdiciones = this.form2.get('checkArray2')?.value.reduce((a : any, b: any) => Number(a) + Number(b), 0);
  }
  
  close(){
      this.modal.dismissAll('reason');
  }
  
  addIngredient(ingredient: Array<string>) {
    this.product['Ingredients'] = ingredient;
  }

  add(){
      this.addIngredient(this.form.get('checkArray')?.value);
      console.log(this.form.get('checkArray')?.value);
      this.productToCart.addProduct(this.product);
      this.modal.dismissAll('reason');
}

}
