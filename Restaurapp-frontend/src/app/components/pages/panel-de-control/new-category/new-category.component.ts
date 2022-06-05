import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { CategoryService } from '@app/shared/services/category.service';

@Component({
  selector: 'app-new-category',
  templateUrl: './new-category.component.html',
  styleUrls: ['./new-category.component.scss']
})
export class NewCategoryComponent implements OnInit {

  constructor(private fb: FormBuilder, private categorySvc: CategoryService) { }
  categoryForm = this.fb.group({
    Name: ['',[Validators.required, Validators.minLength(3), Validators.maxLength(255)]],
    img: ['',[Validators.required, Validators.minLength(3), Validators.maxLength(1000)]]
  });
  ngOnInit(): void {
  }

  onSubmit(){
    console.log(this.categoryForm.value);
    this.categorySvc.postCategory(this.categoryForm.value).subscribe(data => console.log(data));
  }

}

