import { Component, Input, OnInit } from '@angular/core';
import { ProductService } from '@app/shared/services/product.service';

import { FormArray, FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

import { ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {

  product: any;
  ing : String[] = [];
  form : FormGroup;
  @Input() id: number=0;

  constructor(
    private route:ActivatedRoute,
    private productSvc:ProductService,
    private modal: NgbModal,
    private fb: FormBuilder
  ) { 
    this.form = this.fb.group({
      checkArray: this.fb.array([]),
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
  
  close(){
      this.modal.dismissAll('reason');
  }
  
  async addIngredient(ingredient: Array<string>) {
    this.product['Ingredients'] = await ingredient;
  }

  add(){
    this.addIngredient(this.form.value.checkArray);
    console.log(this.product);
    this.close();
  }
}
